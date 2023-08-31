import os

from environs import Env

env = Env()
env.read_env()


def update_access():
    os.system(f'psql %s -U postgres -c "GRANT ALL ON ALL TABLES IN SCHEMA public to %s;"'    % (env.str('DATABASE_NAME'), env.str('DATABASE_USERNAME')))
    os.system(f'psql %s -U postgres -c "GRANT ALL ON ALL SEQUENCES IN SCHEMA public to %s;"' % (env.str('DATABASE_NAME'), env.str('DATABASE_USERNAME')))
    os.system(f'psql %s -U postgres -c "GRANT ALL ON ALL FUNCTIONS IN SCHEMA public to %s;"' % (env.str('DATABASE_NAME'), env.str('DATABASE_USERNAME')))
    os.system(f'psql %s -U postgres -c "GRANT CREATE ON SCHEMA public TO %s;"'    % (env.str('DATABASE_NAME'), env.str('DATABASE_USERNAME')))


def create_database():
    os.system(f'psql -U postgres -c "CREATE DATABASE %s"' % env.str('DATABASE_NAME'))

    
def remove_database():
    os.system(f'psql -U postgres -c "DROP DATABASE %s"' % env.str('DATABASE_NAME'))


def show_description():
    print('Available commands:') 
    print('    db-update-access -- grant previlegies database to env user')
    print('    db-remove        -- remove env database')
    print('    db-create        -- create env database')
    print('    db-recreate      -- recreate env database')


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) <= 1:
        show_description()
    else:
        command = sys.argv[1]
        if command == 'db-update-access':
           update_access() 
        elif command == 'db-remove':
            remove_database()
        elif command == 'db-create':
            create_database()
        elif command == 'db-recreate':
            remove_database()
            create_database()
        else:
            show_description()
