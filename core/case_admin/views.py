from django.shortcuts import render
from accounts.models import User


schema_user = {
    "endpoint": "/api/v1/user",
    "fields": [
        {
            "title": "First Name",
            "key": "first_name",
            "widget": {
                "template": "w-text.html",
                "maxchars": 40,
            },
            "write": True,
        }, {
            "title": "Last Name",
            "key": "last_name",
            "widget": {
                "template": "w-text.html",
                "maxchars": 60,
            },
            "write": True,
        }, {
            "title": "Email",
            "key": "email",
            "widget": {
                "template": "w-email.html",
                "maxchars": 250,
            },
            "write": True,
        }, {
            "title": "University",
            "key": "university",
            "widget": {
                "template": "w-text.html",
                "maxchars": 150,
            },
            "write": True,
        }, {
            "title": "Degree Start",
            "key": "degree_commencement_year",
            "widget": {
                "template": "w-number.html",
            },
            "write": True,
        }, {
            "title": "Is Staff",
            "key": "is_staff",
            "widget": {
                "template": "w-checkbox.html",
                "maxchars": 40,
            },
            "write": True,
        },
    ]
}

schema_case = {
    "endpoint": "/api/v1/case",
    "fields": [],
}

schema_comment = {
    "endpoint": "/api/v1/comment",
    "fields": [],
}

schema_tag = {
    "endpoint": "/api/v1/tag",
    "fields": [],
}

def populate_data(schema, model):
    records = model.objects.all()
    data = {
        "endpoint": schema["endpoint"],
        "fields": [],
    }
    # for all records in the db
    for r in records:
        d = {}  # data to be filled
        # add each field to the data
        for f in schema["fields"]:
            fk = f["key"]
            r[fk] = schema[fk]
            r[fk]["value"] = u[fk]
            r["entity"] = r.id
        data.insert()
    return data


def view_admin_user(request):
    data = populate_data(schema_user, User)
    c = {
        "title": "User Admin",
        "data": data
    }
    return render(request, "case-admin.html", c)


def view_admin_case(request):
    data = populate_data(schema_case, User)
    c = {
        "title": "Case Study Admin",
        "data": data
    }
    return render(request, "case-admin.html", c)


def view_admin_comment(request):
    data = populate_data(schema_comment, User)
    c = {
        "title": "Comment Admin",
        "data": data
    }
    return render(request, "case-admin.html", c)


def view_admin_tag(request):
    data = populate_data(schema_tag, User)
    c = {
        "title": "Tag Admin",
        "data": data
    }
    return render(request, "case-admin.html", c)


def view_default(request):
    return render(request, "admin.html")

