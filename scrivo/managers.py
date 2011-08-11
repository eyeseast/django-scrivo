from model_utils.managers import InheritanceQuerySet

class PostQuerySet(InheritanceQuerySet):
    
    def public(self):
        return self.filter(status=self.model.STATUS.public)
    
    def publish(self):
        """
        Bulk publish all posts in the current queryset.
        Note that this will NOT send pre_ or post_save signals.
        """
        now = datetime.datetime.now()
        count = self.filter(published__isnull=False).update(status=self.model.STATUS.public)
        count += self.filter(published__isnull=True).update(status=self.model.STATUS.public, published=now)
        return count

    def recall(self):
        """
        Silently unpublish all posts in the current queryset
        """
        return self.update(status=self.model.STATUS.hidden)
