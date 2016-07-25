import requests
from django.core.files.base import ContentFile
from django.dispatch import receiver

from allauth.account.signals import user_signed_up


def get_filename_extension(url):
    clean_url = url.split('?')[0]
    filename = clean_url.split('/').pop()
    return filename.split('.').pop()


def download_avatar(user, account):
    url = account.get_avatar_url()
    if not url:
        return

    response = requests.get(url)
    if response.status_code == 200:
        try:
            name = 'avatar_{}.{}'.format(user.id, get_filename_extension(response.url))
            if user.avatar:
                user.avatar.delete()
            user.avatar.save(name, ContentFile(response.content))
        except IOError:
            pass


@receiver(user_signed_up)
def on_user_signed_up(sender, request, *args, **kwargs):
    sociallogin = kwargs.get('sociallogin')
    if sociallogin:
        download_avatar(sociallogin.account.user, sociallogin.account)
