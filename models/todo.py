import sql


class Todo(object):

    def __init__(self):

        pass

    def get_full_list(self):
        return sql.query("SELECT * FROM todo_items")

    def add_item_to_list(self, item):
        """
        :param item:
        :return: None
        """
        query = "INSERT INTO todo_items (`item_title`, `status`) VALUES (?, '0')"
        sql.query(query, list([item]))
        query = "SELECT MAX(ID), * FROM `todo_items`"

        return sql.query(query)

    def toggle(self, item_id):
        """
        :param item_id:
        :return: None
        """

        query = """UPDATE `todo_items` SET
        `status` =  (CASE `status` WHEN 0 THEN 1 WHEN Null THEN 1 ELSE 0 END) WHERE ID={}""".format(item_id)
        sql.query(query)

    def remove(self, item_id):
        """
        :param item_id:
        :return: None
        """

        query = "DELETE FROM `todo_items` WHERE ID={}".format(item_id)
        sql.query(query)

    def update(self, item_id, text_update):
        """
        :param item_id:
        :param text_update
        :return: None
        """

        query = "UPDATE `todo_items` SET item_title=? WHERE ID=?"
        sql.query(query, [text_update, item_id])
        return sql.query("SELECT * FROM todo_items WHERE ID={}".format(item_id))


