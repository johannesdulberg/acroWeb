""" STREAMFIELDS"""

from wagtail.core import blocks
from wagtail.core.blocks import URLBlock, PageChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.blocks.field_block import BooleanBlock


class Navbar(blocks.StructBlock):
    title = blocks.TextBlock(required=True)
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(
        required=False, help_text="If the button page above is selected, that will be used first.")
    item = blocks.ListBlock(
        blocks.StructBlock([
            ("title", blocks.CharBlock(required=True)),
            ("button_page", blocks.PageChooserBlock(required=False)),
            ("button_url", blocks.URLBlock(required=False,
             help_text="If the button page above is selected, that will be used first.")),
        ])
    )

    class Meta:
        icon = "edit"
        label = "Navigationsleiste"
        template = "streams/Navbar.html"


class Header(blocks.StructBlock):
    HEADER = blocks.TextBlock(required=True)
    SUBTITLE = blocks.TextBlock(required=True)
    Button1 = blocks.TextBlock(required=False)
    button1_page = blocks.PageChooserBlock(required=False)
    button1_url = blocks.URLBlock(
        required=False, help_text="If the button page above is selected, that will be used first.")
    Button2 = blocks.TextBlock(required=False)
    button2_page = blocks.PageChooserBlock(required=False)
    button2_url = blocks.URLBlock(
        required=False, help_text="If the button page above is selected, that will be used first.")
    MasterImage = ImageChooserBlock(required=True)

    class Meta:
        template = "streams/Header.html"
        icon = "edit"
        label = "Header"


class ImgAndText(blocks.StructBlock):
    title = blocks.TextBlock(required=True)
    body = blocks.TextBlock(required=True)
    image = ImageChooserBlock(required=True)
    button = blocks.TextBlock(required=False)
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(
        required=False, help_text="If the button page above is selected, that will be used first.")
    reverse = BooleanBlock(required=False)

    class Meta:
        template = "streams/ImgAndText.html"
        icon = "edit"
        label = "Text & Bild"


class TextAndSubtext(blocks.StructBlock):
    title = blocks.TextBlock(required=True)
    body = blocks.TextBlock(required=True)

    class Meta:
        template = "streams/TextAndSubtext.html"
        icon = "edit"
        label = "Titel & Untertitel"


class BigImg(blocks.StructBlock):
    MasterImage = ImageChooserBlock(required=True)

    class Meta:
        template = "streams/BigImg.html"
        icon = "edit"
        label = "Großes Bild"


class Footer(blocks.StructBlock):
    Text = title = blocks.TextBlock(required=True)

    class Meta:
        template = "streams/Footer.html"
        icon = "edit"
        label = "Footer"
