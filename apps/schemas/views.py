from django.shortcuts import render, redirect

from django.views.generic import DetailView, UpdateView
from . import models
from .forms import SchemaForm
from .models import ColumnsSchemas, Schema, TypeCategories


def schemas(request):
    schemas_list = models.Schema.objects.all()
    return render(request, "schemas/schemas.html", {
        "schemas_list": schemas_list,
    })


def create_schemas(request):
    error = ''
    columns = ColumnsSchemas.objects.all()
    if request.method == "POST":
        form = SchemaForm(request.POST)
        if form.is_valid():
            form.save()
            data = Schema.objects.all().last()
            return redirect("update_schemas", id=data.id)
        else:
            error = 'Form was invalid, something wrong. Try again'

    form = SchemaForm()

    data = {
        "columns": columns,
        'form': form,
        'error': error
    }

    return render(request, "schemas/create_schema.html", data)


class SchemaUpdateView(UpdateView):
    model = Schema
    template_name = "schemas/update.html"
    form_class = SchemaForm


def update_schemas(request, id):
    if request.method == "GET":
        data = Schema.objects.get(id=id)
        columns = ColumnsSchemas.objects.filter(cut_schemas_id=id)
        # column = ColumnsSchemas.objects.get(cut_schemas_id=id)
        # type_column = TypeCategories.objects.get(id=column.cut_type_id)
        return render(request, "schemas/update.html", {
            "data": data,
            # "column": column,
            "columns": columns,
            # "type_column": type_column,
        })
    else:
        schema_update = Schema()
        schema_update.title = request.POST.get("title")
        schema_update.column_separator = request.POST.get("column_separator")
        schema_update.string_character = request.POST.get("string_character")
        schema_update.id = id
        Schema.objects.filter(id=id).delete()
        schema_update.save()
        return redirect("schemas")


def update_schemas_columns_add(request, id):
    if request.method == "POST":
        add_column = ColumnsSchemas()
        add_column.name = request.POST.get("name")
        add_column.order = request.POST.get("order")
        # add_column.order = request.POST.get("cut_type_id")
        add_column.cut_type_id = 6
        add_column.cut_schemas_id = id
        add_column.save()
        return redirect("update_schemas", id=id)
    else:
        return render(request, "schemas/update.html", {
            # "categories": categories,
        })


def column_delete(request, pk, id):
    ColumnsSchemas.objects.get(id=id).delete()
    return redirect("update_schemas", id=pk)


def edit_schemas(request, id):
    schema = models.Schema.objects.get(id=id)
    column_separator = models.ColumnSeparator.objects.get(cut_column_separator_id=id)
    string_character = models.StringCharacter.objects.get(cut_string_character_id=id)
    try:
        type_of_schemas_full_name = models.TypeOfSchemasFullname.objects.get(cut_fullname_id=id)
    except:
        type_of_schemas_full_name = ''
    try:
        type_of_schemas_job = models.TypeOfSchemasJob.objects.get(cut_job_id=id)
    except:
        type_of_schemas_job = ''
    try:
        type_of_schemas_email = models.TypeOfSchemasEmail.objects.get(cut_email_id=id)
    except:
        type_of_schemas_email = ''
    try:
        type_of_schemas_domain_name = models.TypeOfSchemasDomainName.objects.get(cut_domain_name_id=id)
    except:
        type_of_schemas_domain_name = ''
    try:
        type_of_schemas_phone_number = models.TypeOfSchemasPhoneNumber.objects.get(cut_phone_number_id=id)
    except:
        type_of_schemas_phone_number = ''
    try:
        type_of_schemas_company_name = models.TypeOfSchemasCompanyName.objects.get(cut_company_name_id=id)
    except:
        type_of_schemas_company_name = ''
    try:
        type_of_schemas_text = models.TypeOfSchemasText.objects.get(cut_text_id=id)
    except:
        type_of_schemas_text = ''
    try:
        type_of_schemas_integer = models.TypeOfSchemasInteger.objects.get(cut_integer_id=id)
    except:
        type_of_schemas_integer = ''
    try:
        type_of_schemas_address = models.TypeOfSchemasAddress.objects.get(cut_address_id=id)
    except:
        type_of_schemas_address = ''
    try:
        type_of_schemas_date = models.TypeOfSchemasDate.objects.get(cut_date_id=id)
    except:
        type_of_schemas_date = ''

    return render(request, "schemas/edit_schema.html", {
        "schema": schema,
        "column_separator": column_separator,
        "string_character": string_character,
        "type_of_schemas_full_name": type_of_schemas_full_name,
        "type_of_schemas_job": type_of_schemas_job,
        "type_of_schemas_email": type_of_schemas_email,
        "type_of_schemas_domain_name": type_of_schemas_domain_name,
        "type_of_schemas_phone_number": type_of_schemas_phone_number,
        "type_of_schemas_company_name": type_of_schemas_company_name,
        "type_of_schemas_text": type_of_schemas_text,
        "type_of_schemas_integer": type_of_schemas_integer,
        "type_of_schemas_address": type_of_schemas_address,
        "type_of_schemas_date": type_of_schemas_date,
    })


