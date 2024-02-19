from pages.back.repositories.list_repository import ListRepository


class ListService:
    list_repository = ListRepository()

    def get_all_lists(self):
        return self.list_repository.get_all_lists()

    def get_by_id(self, list_id):
        if not self.list_repository.exists_by_id(list_id):
            raise RuntimeError

        return self.list_repository.get_by_id(list_id)

    def get_lists_except_for(self, list_id):
        return self.list_repository.get_lists_except_for(list_id)

    def create_list(self, name) -> bool:
        if not name:
            raise RuntimeError

        return self.list_repository.create_list(name)

    def update_by_id(self, list_id, name) -> bool:
        if not self.list_repository.exists_by_id(list_id):
            raise RuntimeError

        return self.list_repository.update_by_id(list_id, name)

    def delete_by_id(self, list_id) -> bool:
        if not self.list_repository.exists_by_id(list_id):
            raise RuntimeError

        return self.list_repository.delete_by_id(list_id)
