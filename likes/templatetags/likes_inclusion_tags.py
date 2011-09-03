from secretballot.models import Vote

from django import template

from likes.utils import can_vote, likes_enabled

register = template.Library()

@register.inclusion_tag('likes/inclusion_tags/likes.html', takes_context=True)
def likes(context, obj):
    request = context['request']
    import_js = False
    if not hasattr(request, '_django_likes_js_imported'):
        setattr(request, '_django_likes_js_imported', 1)
        import_js = True
    can_vote_result, vote_status = can_vote(obj, request.user, request)
    context.update({
        'content_obj': obj,
        'likes_enabled':likes_enabled(obj, request),
        'can_vote': can_vote_result,
        'vote_status': vote_status,
        'content_type': "-".join((obj._meta.app_label, obj._meta.module_name)),
        'import_js': import_js
    })
    return context
