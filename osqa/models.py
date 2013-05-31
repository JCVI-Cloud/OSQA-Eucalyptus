# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=80)
    class Meta:
        db_table = u'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()
    class Meta:
        db_table = u'auth_group_permissions'

class AuthMessage(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    message = models.TextField()
    class Meta:
        db_table = u'auth_message'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)
    class Meta:
        db_table = u'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=128)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    is_superuser = models.BooleanField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = u'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()
    class Meta:
        db_table = u'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    permission_id = models.IntegerField()
    class Meta:
        db_table = u'auth_user_user_permissions'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user_id = models.IntegerField()
    content_type_id = models.IntegerField()
    object_id = models.TextField()
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = u'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        db_table = u'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = u'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = u'django_site'

class ForumAction(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    real_user_id = models.IntegerField()
    ip = models.CharField(max_length=16)
    node_id = models.IntegerField()
    action_type = models.CharField(max_length=16)
    action_date = models.DateTimeField()
    extra = models.TextField()
    canceled = models.BooleanField()
    canceled_by_id = models.IntegerField()
    canceled_at = models.DateTimeField()
    canceled_ip = models.CharField(max_length=16)
    class Meta:
        db_table = u'forum_action'

class ForumActionrepute(models.Model):
    id = models.IntegerField(primary_key=True)
    action_id = models.IntegerField()
    by_canceled = models.BooleanField()
    value = models.IntegerField()
    user_id = models.IntegerField()
    date = models.DateTimeField()
    class Meta:
        db_table = u'forum_actionrepute'

class ForumAuthkeyuserassociation(models.Model):
    id = models.IntegerField(primary_key=True)
    added_at = models.DateTimeField()
    user_id = models.IntegerField()
    key = models.CharField(max_length=255)
    provider = models.CharField(max_length=64)
    class Meta:
        db_table = u'forum_authkeyuserassociation'

class ForumAward(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    badge_id = models.IntegerField()
    node_id = models.IntegerField()
    awarded_at = models.DateTimeField()
    trigger_id = models.IntegerField()
    action_id = models.IntegerField(unique=True)
    class Meta:
        db_table = u'forum_award'

class ForumBadge(models.Model):
    id = models.IntegerField(primary_key=True)
    awarded_count = models.IntegerField()
    type = models.IntegerField()
    cls = models.CharField(max_length=50)
    class Meta:
        db_table = u'forum_badge'

class ForumFlag(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    node_id = models.IntegerField()
    reason = models.CharField(max_length=300)
    action_id = models.IntegerField(unique=True)
    flagged_at = models.DateTimeField()
    class Meta:
        db_table = u'forum_flag'

class ForumKeyvalue(models.Model):
    id = models.IntegerField(primary_key=True)
    value = models.TextField()
    key = models.CharField(max_length=255)
    class Meta:
        db_table = u'forum_keyvalue'

class ForumMarkedtag(models.Model):
    id = models.IntegerField(primary_key=True)
    tag_id = models.IntegerField()
    user_id = models.IntegerField()
    reason = models.CharField(max_length=16)
    class Meta:
        db_table = u'forum_markedtag'

class ForumNode(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=300)
    tagnames = models.CharField(max_length=125)
    author_id = models.IntegerField()
    body = models.TextField()
    node_type = models.CharField(max_length=16)
    parent_id = models.IntegerField()
    abs_parent_id = models.IntegerField()
    added_at = models.DateTimeField()
    score = models.IntegerField()
    state_string = models.TextField()
    last_edited_id = models.IntegerField(unique=True)
    last_activity_by_id = models.IntegerField()
    last_activity_at = models.DateTimeField()
    active_revision_id = models.IntegerField(unique=True)
    extra = models.TextField()
    extra_ref_id = models.IntegerField()
    extra_count = models.IntegerField()
    marked = models.BooleanField()
    class Meta:
        db_table = u'forum_node'

class ForumNodeTags(models.Model):
    id = models.IntegerField(primary_key=True)
    node_id = models.IntegerField()
    tag_id = models.IntegerField()
    class Meta:
        db_table = u'forum_node_tags'

class ForumNoderevision(models.Model):
    id = models.IntegerField(primary_key=True)
    node_id = models.IntegerField()
    body = models.TextField()
    author_id = models.IntegerField()
    tagnames = models.CharField(max_length=125)
    title = models.CharField(max_length=300)
    summary = models.CharField(max_length=300)
    revised_at = models.DateTimeField()
    revision = models.IntegerField()
    class Meta:
        db_table = u'forum_noderevision'

class ForumNodestate(models.Model):
    id = models.IntegerField(primary_key=True)
    node_id = models.IntegerField()
    state_type = models.CharField(max_length=16)
    action_id = models.IntegerField(unique=True)
    class Meta:
        db_table = u'forum_nodestate'

class ForumOpenidassociation(models.Model):
    id = models.IntegerField(primary_key=True)
    server_url = models.TextField()
    handle = models.CharField(max_length=255)
    secret = models.TextField()
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.TextField()
    class Meta:
        db_table = u'forum_openidassociation'

class ForumOpenidnonce(models.Model):
    id = models.IntegerField(primary_key=True)
    server_url = models.CharField(max_length=200)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=50)
    class Meta:
        db_table = u'forum_openidnonce'

class ForumQuestionsubscription(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    question_id = models.IntegerField()
    auto_subscription = models.BooleanField()
    last_view = models.DateTimeField()
    class Meta:
        db_table = u'forum_questionsubscription'

class ForumSubscriptionsettings(models.Model):
    id = models.IntegerField(primary_key=True)
    questions_viewed = models.BooleanField()
    notify_comments = models.BooleanField()
    new_question = models.CharField(max_length=1)
    all_questions = models.BooleanField()
    new_question_watched_tags = models.CharField(max_length=1)
    notify_comments_own_post = models.BooleanField()
    subscribed_questions = models.CharField(max_length=1)
    notify_reply_to_comments = models.BooleanField()
    member_joins = models.CharField(max_length=1)
    user_id = models.IntegerField()
    notify_answers = models.BooleanField()
    enable_notifications = models.BooleanField()
    all_questions_watched_tags = models.BooleanField()
    notify_accepted = models.BooleanField()
    send_digest = models.BooleanField()
    class Meta:
        db_table = u'forum_subscriptionsettings'

class ForumTag(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    created_by_id = models.IntegerField()
    created_at = models.DateTimeField()
    used_count = models.IntegerField()
    class Meta:
        db_table = u'forum_tag'

class ForumUser(models.Model):
    user_ptr_id = models.IntegerField(primary_key=True)
    is_approved = models.BooleanField()
    email_isvalid = models.BooleanField()
    reputation = models.IntegerField()
    gold = models.IntegerField()
    silver = models.IntegerField()
    bronze = models.IntegerField()
    last_seen = models.DateTimeField()
    real_name = models.CharField(max_length=100)
    website = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    about = models.TextField()
    class Meta:
        db_table = u'forum_user'

class ForumUserproperty(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    key = models.CharField(max_length=16)
    value = models.TextField()
    class Meta:
        db_table = u'forum_userproperty'

class ForumValidationhash(models.Model):
    id = models.IntegerField(primary_key=True)
    hash_code = models.CharField(max_length=255)
    seed = models.CharField(max_length=12)
    expiration = models.DateTimeField()
    type = models.CharField(max_length=12)
    user_id = models.IntegerField()
    class Meta:
        db_table = u'forum_validationhash'

class ForumVote(models.Model):
    id = models.IntegerField(primary_key=True)
    node_id = models.IntegerField()
    action_id = models.IntegerField()
    value = models.IntegerField()
    user_id = models.IntegerField()
    voted_at = models.DateTimeField()
    class Meta:
        db_table = u'forum_vote'

class SouthMigrationhistory(models.Model):
    id = models.IntegerField(primary_key=True)
    app_name = models.CharField(max_length=255)
    migration = models.CharField(max_length=255)
    applied = models.DateTimeField()
    class Meta:
        db_table = u'south_migrationhistory'

