import sql


class todo_list(object):


    @staticmethod
    def get_full_list():
        return sql.query("SELECT * FROM todo_items")

    @staticmethod
    def add_item_to_list(item):
        """
        :param item:
        :return: None
        """
        query = "INSERT INTO todo_items (`item_title`, `status`) VALUES (?, '0')"
        sql.query(query, list([item]))
        query = "SELECT MAX(ID), * FROM `todo_items`"

        return sql.query(query)

    @staticmethod
    def toggle(item_id):
        """
        :param item_id:
        :return: None
        """

        query = """UPDATE `todo_items` SET
        `status` =  (CASE `status` WHEN 0 THEN 1 WHEN Null THEN 1 ELSE 0 END) WHERE ID={}""".format(item_id)
        sql.query(query)

    @staticmethod
    def remove(item_id):
        """
        :param item_id:
        :return: None
        """

        query = "DELETE FROM `todo_items` WHERE ID={}".format(item_id)
        sql.query(query)