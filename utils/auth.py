import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import bcrypt
import os

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def load_auth():
    config_path = "auth_config.yaml"

    if not os.path.exists(config_path):
        default_config = {
            'credentials': {
                'usernames': {
                    'priyanshu': {
                        'email': 'priyanshukv06@gmail.com',
                        'first_name': 'Priyanshu',
                        'last_name': 'Verma',
                        'password': hash_password('admin123'),
                        'roles': ['admin']
                    }
                }
            },
            'cookie': {
                'expiry_days': 30,
                'key': 'popcornpicks_secret_key_xyz123',
                'name': 'popcornpicks_cookie'
            },
            'pre-authorized': {
                'emails': ['priyanshukv06@gmail.com']
            }
        }
        with open(config_path, 'w') as f:
            yaml.dump(default_config, f)

    with open(config_path) as f:
        config = yaml.load(f, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days']
    )
    return authenticator, config, config_path


def login_page():
    authenticator, config, config_path = load_auth()
    
    # v0.4.x API — returns nothing, reads from session_state
    authenticator.login()

    auth_status = st.session_state.get('authentication_status')
    username    = st.session_state.get('username')
    name        = st.session_state.get('name')

    return authenticator, name, auth_status, username, config, config_path
