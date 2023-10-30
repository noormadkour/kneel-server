"""Orders placed module"""
import json
from nss_handler import status
from repository import db_get_all, db_get_single


class OrdersView:
    def get(self, handler, url):
        """ Method for handling HTTP request to GET all orders @ /orders
        Args:
            handler: http handler to handle the request and return a response
            url: will be indexed into for query_params, and pk
        Returns:
            response from handler        
        """
        sql = "SELECT o.id, o.metalId, o.styleId, o.sizeId FROM Orders o"

        if url["pk"] != 0:
            sql += " WHERE o.id = ?"
            query_results = db_get_single(sql, url["pk"])
            serialized_orders = json.dumps(dict(query_results))
        else:
            query_results = db_get_all(sql, url["pk"])
            orders = [dict(row) for row in query_results]
            serialized_orders = json.dumps(orders)

        return handler.response(serialized_orders, status.HTTP_200_SUCCESS.value)