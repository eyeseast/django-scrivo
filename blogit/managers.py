from model_utils.managers import InheritanceQuerySet

class PostQuerySet(InheritanceQuerySet):
    
    def public(self):
        return self.filter(status=self.model.STATUS.public)