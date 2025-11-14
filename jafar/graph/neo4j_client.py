from neo4j import GraphDatabase, RoutingControl
from typing import Optional
import structlog
from jafar.config import config

logger = structlog.get_logger()

class Neo4jClient:
    def __init__(self):
        self.driver = GraphDatabase.driver(config.NEO4J_URI, auth=(config.NEO4J_USER, config.NEO4J_PASSWORD))

    def close(self):
        self.driver.close()

    def create_entities(self, company: str, officer: str, event: str, risk: float):
        query = (
            "MERGE (c:Company {name: $company}) "
            "MERGE (o:Officer {name: $officer}) "
            "MERGE (e:Event {description: $event}) "
            "MERGE (r:Risk {score: $risk}) "
            "MERGE (c)-[:HAS_OFFICER]->(o) "
            "MERGE (o)-[:INVOLVED_IN]->(e) "
            "MERGE (e)-[:LEADS_TO]->(r)"
        )
        self.driver.execute_query(query, company=company, officer=officer, event=event, risk=risk, database_="neo4j")
        logger.info(f"Created graph nodes for {company}")

    # More queries...