from blog import app 
import unittest

class FlaskTestCase(unittest.TestCase):
    
    # ensure that Flask was setup correctly
    def test_index(self):
        tester = app.test_client()
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    
    # ensure that login page loads correctly
    def test_login_page_loads(self):
        tester = app.test_client()
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Please login' in response.data)
    
    # ensure that login works correctly with good credentials
    def test_correct_login(self):
        tester = app.test_client()
        response = tester.post(
            '/login',
            data=dict(username="admin", password="admin"),
            follow_redirects =True)        
        self.assertTrue(b'You were just logged in' in response.data)
        
    # ensure that login works correctly with invalid credentials
    def test_incorrect_login(self):
        tester = app.test_client()
        response = tester.post(
            '/login',
            data=dict(username="", password=""),
            follow_redirects =True)        
        self.assertTrue(b'Invalid credentials, please try again!' in response.data)
    
    # ensure that logout works correctly
    def test_logout(self):
        tester = app.test_client()
        response = tester.post(
            '/login',
            data=dict(username="admin", password="admin"),
            follow_redirects =True)
        response = tester.get('/logout', follow_redirects=True)
        self.assertTrue(b'You were just logged out!' in response.data)
    
    # ensure that main page requires login
    def test_main_route_require_login(self):
        tester = app.test_client()
        response = tester.get('/', follow_redirects=True)
        self.assertTrue(b'You need to login first' in response.data)
        
    # ensure that logout page requires login
    def test_logout_route_require_login(self):
        tester = app.test_client()
        response = tester.get('/logout', follow_redirects=True)
        self.assertTrue(b'You need to login first' in response.data)
    
    # ensure that posts show up on the main page
    def test_post_show_up(self):
        tester = app.test_client()
        response = tester.post(
            '/login',
            data=dict(username="admin", password="admin"),
            follow_redirects =True)
        response = tester.get('/')
        self.assertTrue(b'alchemyTitle' in response.data)
        
    
if __name__ == '__main__':
    unittest.main()
