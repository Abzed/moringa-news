from django.test import TestCase
from .models import Editor,Article,tags
import datetime as dt

class EditorTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.abzed= Editor(first_name = 'Abzed', last_name ='tet', email ='ibraabzed@gmail.com')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.abzed,Editor))
        
    def test_save_method(self):
        self.abzed.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)
        
class ArticleTestClass(TestCase):
    
    def setUp(self):
        # Creating a new editor and saving it
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)
        
    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()
