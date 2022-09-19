from typing import Any
from datetime import datetime

from pydantic import BaseModel, Json, conint, conlist


class Field(BaseModel):
    # 根组件
    __root__: Any


class TextField(Field):
    # 单行文本
    __root__: str


class TextAreaField(Field):
    # 多行文本
    __root__: str


class NumberField(Field):
    # 数值
    __root__: float


class RadioField(Field):
    # 单选
    __root__: str


class CheckboxField(Field):
    # 复选
    __root__: list[str]


class RateField(Field):
    # 评分
    __root__: conint(ge=1, le=100)


class SelectField(Field):
    # 下拉单选
    __root__: str


class MultiSelectField(Field):
    # 下拉复选
    __root__: list[str]


class CascadeSelectField(Field):
    # 级联选择
    __root__: list[str]


class DateField(Field):
    # 日期
    __root__: datetime


class CascadeDateField(Field):
    # 日期区间
    __root__: conlist(datetime, min_items=2, max_items=2)


class ImageField(Field):
    # 图片上传
    class ImageFieldContent(BaseModel):
        previewUrl: str
        size: int
        name: str
        downloadUrl: str
        url: str

    __root__: Json[list[ImageFieldContent]]


class AttachmentField(Field):
    class AttachmentFieldContent(BaseModel):
        downloadUrl: str
        name: str
        previewUrl: str
        url: str
        ext: str

    # 附件组件
    __root__: Json[list[AttachmentFieldContent]]


class EmployeeField(Field):
    # 成员
    __root__: list[str]


class TableField(Field):
    # 子表单组件
    __root__: Json[list[dict[str, Field]]]


class DepartmentSelectField(Field):
    # 部门
    __root__: list[str]


class CountrySelectField(Field):
    # 国家/地区
    __root__: Json[list[dict]]


class AddressField(Field):
    # 地址
    class AddressFieldContent(BaseModel):
        class RegionText(BaseModel):
            en_US: str
            zh_CN: str

        address: str
        regionIds: list[str]
        regionText: list[RegionText]

    __root__: Json[AddressFieldContent]


class EditorField(Field):
    # 富文本
    __root__: str


class CityField(Field):
    # 城市选择
    __root__: list[str]


class LinkField(Field):
    # 超链接
    class LinkFieldContent(BaseModel):
        link: str
        text: str

    __root__: Json[list[LinkFieldContent]]


class AssociationFormField(Field):
    # 关联表单
    class AssociatedFormContent(BaseModel):
        appType: str
        formUuid: str
        formType: str = 'receipt'
        instanceId: str
        title: str
        subTitle: str | None = None

    __root__: Json[list[AssociatedFormContent]]


__all__ = [
    'Field',
    'TextField',
    'TextAreaField',
    'NumberField',
    'RadioField',
    'CheckboxField',
    'RateField',
    'SelectField',
    'MultiSelectField',
    'CascadeSelectField',
    'DateField',
    'CascadeDateField',
    'ImageField',
    'AttachmentField',
    'EmployeeField',
    'TableField',
    'DepartmentSelectField',
    'CountrySelectField',
    'AddressField',
    'EditorField',
    'CityField',
    'LinkField',
    'AssociationFormField'
]
