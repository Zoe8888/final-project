import unittest
from app import app


# Testing response codes
class App(unittest.TestCase):
    def test_registration(self):
        test = app.test_client(self)
        response = test.get('/registration/')
        status = response.status_code
        self.assertEqual(status, 400)

    def test_send_email(self):
        test = app.test_client(self)
        response = test.get('/send-email/<email>')
        status = response.status_code
        self.assertEqual(status, 200)

    def test_login(self):
        test = app.test_client(self)
        response = test.get('/login/')
        status = response.status_code
        self.assertEqual(status, 200)

    def test_view_profile(self):
        test = app.test_client(self)
        response = test.get('/view-profile/<username>//')
        status = response.status_code
        self.assertEqual(status, 200)

    def test_edit_profile(self):
        test = app.test_client(self)
        response = test.get('/edit-profile/<username>/')
        status = response.status_code
        self.assertEqual(status, 400)

    def test_delete_profile(self):
        test = app.test_client(self)
        response = test.get('/delete-profile/<username>/')
        status = response.status_code
        self.assertEqual(status, 200)

    def test_display_users(self):
        test = app.test_client(self)
        response = test.get('/display-users/')
        status = response.status_code
        self.assertEqual(status, 200)

    def test_create_post(self):
        test = app.test_client(self)
        response = test.get('/create-post/')
        status = response.status_code
        self.assertEqual(status, 400)

    def test_delete_post(self):
        test = app.test_client(self)
        response = test.get('/delete-post/<int:post_id>')
        status = response.status_code
        self.assertEqual(status, 200)

    def test_edit_post(self):
        test = app.test_client(self)
        response = test.get('/edit-post/<int:post_id>/')
        status = response.status_code
        self.assertEqual(status, 400)

    def test_show_posts(self):
        test = app.test_client(self)
        response = test.get('/show-posts/')
        status = response.status_code
        self.assertEqual(status, 200)

    def test_view_post(self):
        test = app.test_client(self)
        response = test.get('/view-post/<int:post_id>/')
        status = response.status_code
        self.assertEqual(status, 200)

    def test_view_users_posts(self):
        test = app.test_client(self)
        response = test.get('/view-users-posts/<int:id>/')
        status = response.status_code
        self.assertEqual(status, 200)

    def test_like_post(self):
        test = app.test_client(self)
        response = test.get('/like-post/')
        status = response.status_code
        self.assertEqual(status, 400)

    def test_unlike_post(self):
        test = app.test_client(self)
        response = test.get('/like-post/')
        status = response.status_code
        self.assertEqual(status, 200)

    def test_display_likes(self):
        test = app.test_client(self)
        response = test.get('/display-likes/<int:post_id>/')
        status = response.status_code
        self.assertEqual(status, 200)

    def test_add_comment(self):
        test = app.test_client(self)
        response = test.get('/add-comment/')
        status = response.status_code
        self.assertEqual(status, 400)

    def test_edit_comment(self):
        test = app.test_client(self)
        response = test.get('/edit-comment/<int:comment_id>/')
        status = response.status_code
        self.assertEqual(status, 400)

    def test_delete_comment(self):
        test = app.test_client(self)
        response = test.get('/delete-comment/<int:comment_id>/')
        status = response.status_code
        self.assertEqual(status, 200)

    def test_search(self):
        test = app.test_client(self)
        response = test.get('/search/<post_query>/')
        status = response.status_code
        self.assertEqual(status, 200)


if __name__ == '__main__':
    unittest.main()
