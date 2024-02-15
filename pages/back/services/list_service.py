from pages.back.repositories.list_repository import ListRepository


class ListService:
    list_repository = ListRepository()

    def get_all_lists(self):
        items = self.list_repository.get_all_lists()
        return items
