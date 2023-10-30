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
            order_dictionary = dict(query_results)
            if "_expand" in url["query_params"] and "metal" in url["query_params"]["_expand"]:
                metal_fk = order_dictionary["metalId"]
                metal_sql = "SELECT m.id, m.metal, m.price From Metals m WHERE m.id = ?"
                metal_info = db_get_single(metal_sql, metal_fk)
                metal_object = {
                    "id": metal_info["id"],
                    "metal": metal_info["metal"],
                    "price": metal_info["price"]
                }
                order_dictionary["metal"] = metal_object
            if "_expand" in url["query_params"] and "style" in url["query_params"]["_expand"]:
                style_fk = order_dictionary["styleId"]
                style_sql = "SELECT s.id, s.style, s.price From Styles s WHERE s.id = ?"
                style_info = db_get_single(style_sql, style_fk)
                style_object = {
                    "id": style_info["id"],
                    "style": style_info["style"],
                    "price": style_info["price"]
                }
                order_dictionary["style"] = style_object
            if "_expand" in url["query_params"] and "size" in url["query_params"]["_expand"]:
                size_fk = order_dictionary["sizeId"]
                size_sql = "SELECT s.id, s.carets, s.price From Sizes s WHERE s.id = ?"
                size_info = db_get_single(size_sql, size_fk)
                size_object = {
                    "id": size_info["id"],
                    "carets": size_info["carets"],
                    "price": size_info["price"]
                }
                order_dictionary["size"] = size_object
            
            serialized_orders = json.dumps(order_dictionary)
        else:
            query_results = db_get_all(sql, url["pk"])
            orders = [dict(row) for row in query_results]
            serialized_orders = json.dumps(orders)

        return handler.response(serialized_orders, status.HTTP_200_SUCCESS.value)