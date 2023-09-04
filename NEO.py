from neo4j import GraphDatabase

# Define a class to interact with the Neo4j database
class Neo4jHandler:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def create_node(self, name):
        with self._driver.session() as session:
            session.write_transaction(self._create_node, name)

    @staticmethod
    def _create_node(tx, name):
        query = (
            "CREATE (n:Person {name: $name})"
            "RETURN n"
        )
        result = tx.run(query, name=name)
        return result.single()

    def get_nodes(self):
        with self._driver.session() as session:
            return session.read_transaction(self._get_nodes)

    @staticmethod
    def _get_nodes(tx):
        query = (
            "MATCH (n:Person)"
            "RETURN n.name AS name"
        )
        result = tx.run(query)
        return [record["name"] for record in result]

# Example usage
if __name__ == "__main__":
    neo4j_uri = "bolt://localhost:7687"  # Replace with your Neo4j server URI
    neo4j_user = "neo4j"  # Replace with your Neo4j username
    neo4j_password = "your_password"  # Replace with your Neo4j password

    neo4j_handler = Neo4jHandler(neo4j_uri, neo4j_user, neo4j_password)

    # Create nodes
    neo4j_handler.create_node("Alice")
    neo4j_handler.create_node("Bob")

    # Retrieve nodes
    nodes = neo4j_handler.get_nodes()
    print("Nodes in the database:", nodes)

    # Close the connection
    neo4j_handler.close()
