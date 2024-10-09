from IMedia import IMedia
from database.IDBManager import IDBManager

class MediaManager:
   
    def __init__(self, db_manager: IDBManager):
        self.db_manager = db_manager
  
    def add_media(self, media):
        
        if isinstance(media, IMedia):
            self.db_manager.create(media)
            print(f"Livre ajouté : {media}")

    def list_available_madias(self):
        available_medias = [media for media in self.medias if media.is_available()]
        if available_medias:
            print("Medias disponibles :")
            for media in available_medias:
                print(f"- {media}")
        else:
            print("Aucun livre disponible.")

    def find_media(self, title):
        for media in self.medias:
            if media.title == title:
                return media
        return None
