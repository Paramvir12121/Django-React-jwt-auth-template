# Django-React-jwt-auth-template
This is a template containing boilerplate react and django application with authentication set up



Dealing with jasmine logout not working:
Follow these steps:

1. Navigate to the template file where the Django-Jazzmin admin interface is being customized. This is usually located at /rootProject/templates/admin/base.html.

2. Locate the logout link in the template. It may look something like this:
```
<a href="{% url 'admin:logout' %}" class="dropdown-item">
    <i class="fas fa-users mr-2"></i> {% trans 'Log out' %}
</a>
```
3. Replace the above code with a form submission:
```
<form action="{% url 'admin:logout' %}" method="post">
    {% csrf_token %}
    <button type="submit" class="dropdown-item">
        <i class="fas fa-users mr-2"></i> {% trans 'Log out' %}
    </button>
</form>
```
4. Save the changes to the base.html file.
By replacing the logout link with a form submission, you ensure that the logout operation is performed via a POST request, which is the expected method for sensitive operations like logging out. This should resolve the 405 error you're encountering when trying to log out from the admin page.

Soluton by Bercove @ stack overflow 
https://stackoverflow.com/questions/77987598/how-to-solve-logout-error-when-using-django-jazzmin