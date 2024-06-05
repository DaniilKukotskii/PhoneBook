from model.phone_directory import PhoneDirectory
from view.phone_directory_view import PhoneDirectoryView
from presenter.phone_directory_presenter import PhoneDirectoryPresenter

def main():
    phone_directory = PhoneDirectory()
    phone_directory_presenter = PhoneDirectoryPresenter(phone_directory, None)
    phone_directory_view = PhoneDirectoryView(phone_directory_presenter)
    phone_directory_presenter.view = phone_directory_view

    phone_directory_view.user_interface()

if __name__ == "__main__":
    main()
