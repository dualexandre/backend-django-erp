from rest_framework.exceptions import AuthenticationFailed, APIException
from django.contrib.auth.hashers import check_password, make_password
from accounts.models import User
from companies.models import Enterprise, Employee

class Authentication:
    def signin(self, email=None, password=None) -> User:
        exception_auth = AuthenticationFailed('Email e/ou senha incorreto(s)')

        user_exists = User.objects.filter(email=email).exists()
        if not user_exists:
            raise exception_auth
        
        user = User.objects.filter(email=email).first()
        if not check_password(password, user.password):
            raise exception_auth
        
        return user
    
    def signup(self, name, email, password, type_account='owner', company_name='Nome da Empresa', company_id=False) -> User:
        if not name or name == '':
            raise APIException('O nome não deve ser nulo')
        
        if not email or email == '':
            raise APIException('O email não deve ser nulo')
        
        if not password or password == '':
            raise APIException('A senha não deve ser nula')
        
        if type_account == 'employee' and not company_id:
            raise APIException('O id da empresa não deve ser nulo')
        
        user_exists = User.objects.filter(email=email).exists()
        if user_exists:
            raise APIException('Este email já está cadastrado')
        
        password_hashed = make_password(password)

        create_user = User.objects.create(
            name=name,
            email=email,
            password=password_hashed,
            is_owner=0 if type_account == 'employee' else 1
        )

        enterprise_id = company_id
        if type_account == 'owner':
            enterprise = Enterprise.objects.create(
                name=company_name,
                user_id=create_user.id
            )

            enterprise_id = enterprise.id

        if type_account == 'employee':
            Employee.objects.create(
                user_id=create_user.id,
                enterprise_id=enterprise_id
            )

        return create_user
