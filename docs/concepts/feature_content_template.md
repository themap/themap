# Feature content template

Feature content supports the rich media format to be displayed. To provide rich media, input should be in following format.

## Template Format
    [
        'type:value',
        'type:value',
        'type:value'
    ]

## Explanation

So template would be an array containing any number of elements. Media being rendered will follow the same sequence as provided in an array.

* `type` - Possible value : `heading`,`link`,`image`,`anchor`,`content` or `video`
* `value` - In case of heading, it will be heading text. In case of link, image or video, it will be url of the link/media. In case of anchor it should be | seprated anchor name and link. e.g. `Anchor Name|https://anchor.link`. In case of content, it will be any text or html

## Example

    [
        'heading:This is cool heading',
        'image:https://www.link.to/hero-image.png',
        'link:https://www.visit.this/link/to/know/more',
        'heading:How about another heading?',
        'anchor:Follow This Link|https://themap.net',
        'content:Some text that goes as paragraph',
    ]