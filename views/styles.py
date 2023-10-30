"""Style options module"""
import json
from nss_handler import status
from repository import db_get_all, db_get_single


class StylesView:
    def get(self, handler, url):
        """ Method for handling HTTP request to GET all styles @ /styles
        Args:
            handler: http handler to handle the request and return a response
            url: will be indexed into for query_params, and pk
        Returns:
            response from handler        
        """
        sql = "SELECT sy.id, sy.style, sy.price FROM Styles sy"

        if url["pk"] != 0:
            sql += " WHERE sy.id = ?"
            query_results = db_get_single(sql, url["pk"])
            serialized_styles = json.dumps(dict(query_results))
        else:
            query_results = db_get_all(sql, url["pk"])
            styles = [dict(row) for row in query_results]
            serialized_styles = json.dumps(styles)

        return handler.response(serialized_styles, status.HTTP_200_SUCCESS.value)