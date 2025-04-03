from fastapi import APIRouter, Query
from typing import Optional
from datetime import date
import psycopg2
import os

router = APIRouter(prefix="/conversao", tags=["Taxa de Conversão"])

DB_CONFIG = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASS"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT")
}

@router.get("/")
def get_taxa_conversao(
    canal: Optional[str] = Query(None),
    data_inicio: Optional[date] = Query(None),
    data_fim: Optional[date] = Query(None)
):
    conn = None
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Montagem da query dinâmica
        base_query = """
        SELECT
            DATE(created_at) as data,
            origin,
            COUNT(*) FILTER (WHERE response_status_id = 6) * 1.0 / COUNT(*) AS taxa_conversao
        FROM inside.users_surveys_responses_aux
        WHERE 1=1
        """
        params = []

        if canal:
            base_query += " AND origin = %s"
            params.append(canal)

        if data_inicio:
            base_query += " AND created_at >= %s"
            params.append(data_inicio)

        if data_fim:
            base_query += " AND created_at <= %s"
            params.append(data_fim)

        base_query += " GROUP BY data, origin ORDER BY data, origin"

        cursor.execute(base_query, tuple(params))
        rows = cursor.fetchall()

        resultado = [
            {
                "data": row[0].isoformat(),
                "canal": row[1],
                "taxa_conversao": float(row[2])
            }
            for row in rows
        ]

        return resultado

    except Exception as e:
        return {"erro": str(e)}

    finally:
        if conn:
            conn.close()
