from django.db import models


class Schema(models.Model):
    title = models.CharField(max_length=255)
    column_separator = models.CharField(max_length=1, default=";")
    string_character = models.CharField(max_length=1, default="'")
    modified = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class ColumnSeparator(models.Model):
    column_separator = models.CharField(max_length=1)
    cut_column_separator = models.ForeignKey(Schema, on_delete=models.CASCADE)

    def __str__(self):
        return self.column_separator


class StringCharacter(models.Model):
    string_character = models.CharField(max_length=1)
    cut_string_character = models.ForeignKey(Schema, on_delete=models.CASCADE)

    def __str__(self):
        return self.string_character


class TypeOfSchemasFullname(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cut_fullname = models.ForeignKey(Schema, on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name


class TypeOfSchemasJob(models.Model):
    job = models.CharField(max_length=255)
    cut_job = models.ForeignKey(Schema, on_delete=models.CASCADE)

    def __str__(self):
        return self.job


class TypeOfSchemasEmail(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    cut_email = models.ForeignKey(Schema, on_delete=models.CASCADE)

    def __str__(self):
        return self.email


class TypeOfSchemasDomainName(models.Model):
    domain_name = models.CharField(max_length=255)
    cut_domain_name = models.ForeignKey(Schema, on_delete=models.CASCADE)

    def __str__(self):
        return self.domain_name


class TypeOfSchemasPhoneNumber(models.Model):
    phone_number = models.CharField(max_length=13)
    cut_phone_number = models.ForeignKey(Schema, on_delete=models.CASCADE)

    def __str__(self):
        return self.phone_number


class TypeOfSchemasCompanyName(models.Model):
    company_name = models.CharField(max_length=255)
    cut_company_name = models.ForeignKey(Schema, on_delete=models.CASCADE)

    def __str__(self):
        return self.company_name


class TypeOfSchemasText(models.Model):
    text = models.TextField()
    cut_text = models.ForeignKey(Schema, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class TypeOfSchemasInteger(models.Model):
    integer_start = models.IntegerField()
    integer_finish = models.IntegerField()
    cut_integer = models.ForeignKey(Schema, on_delete=models.CASCADE)

    def __int__(self):
        return self.integer_start


class TypeOfSchemasAddress(models.Model):
    address = models.TextField()
    cut_address = models.ForeignKey(Schema, on_delete=models.CASCADE)

    def __str__(self):
        return self.address


class TypeOfSchemasDate(models.Model):
    date = models.DateField()
    cut_date = models.ForeignKey(Schema, on_delete=models.CASCADE)

    def _perform_date_checks__(self):
        return self.date


class ColumnSeparatorView(models.Model):
    column_separator_view = models.CharField(max_length=1)

    def __str__(self):
        return self.column_separator_view


class StringCharacterView(models.Model):
    string_character_view = models.CharField(max_length=1)

    def __str__(self):
        return self.string_character_view


class TypeCategories(models.Model):
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.type


class ColumnsSchemas(models.Model):
    name = models.CharField(max_length=255, null=True)
    order = models.IntegerField(default=0, null=True)
    cut_type = models.ForeignKey(TypeCategories, on_delete=models.CASCADE)
    cut_schemas = models.ForeignKey(Schema, on_delete=models.CASCADE)

    def __str__(self):
        return self.cut_type.type + " ---- " + self.cut_schemas.title