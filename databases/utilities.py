# -*- coding: utf-8 -*-

# import modules
import re

# typing
from typing import Dict, Tuple

'''
Extract likes and comments from snippet

'''
def extract_likes_comments(text: str) -> Tuple:
    '''
    Extracts likes and comments from a given text.

    :param text: The text containing likes and comments.
    :return: A tuple containing the extracted likes and comments, or None if
        not found.
    '''
    # define regex patterns for likes and comments
    likes_pattern = re.compile(
        r'(\d+(?:[\d,.]*\d+)?(?:[KM])?) Likes',
        re.IGNORECASE
    )

    comments_pattern = re.compile(
        r'(\d+(?:[\d,.]*\d+)?(?:[KM])?) Comments',
        re.IGNORECASE
    )

    # search for likes and comments in the text
    likes_match = likes_pattern.search(text)
    comments_match = comments_pattern.search(text)

    # extract the matched groups or return None if not found
    likes = likes_match.group(1) if likes_match else None
    comments = comments_match.group(1) if comments_match else None

    return likes, comments

'''
Extract fields from the field link

'''
def extract_author_post_id(link: str) -> Tuple:
    '''
    Extracts the author, link to the author's page, and post ID from a TikTok
    video link.

    :param link: The TikTok video link.
    :return: A tuple containing the author's username, link to the author's
        page, and the post ID.
    '''
    author = link.split('/')[3].replace('@', '')
    link_to_author = f'https://www.tiktok.com/@{author}'
    post_id = link.split('/')[-1]

    return author, link_to_author, post_id

'''
Get items and keys from search results entries

'''
def get_items_from_search_results(entry: Dict) -> Tuple:
    '''
    Extracts and processes specific fields from a data entry.

    :param entry: A dictionary containing the data entry.
    :return: A tuple containing the extracted and processed values for the
        fields.
    '''
    # get values
    title = entry.get('title', '')
    snippet = entry.get('snippet', '')
    link = entry.get('link', '')

    # process new fields from data
    likes, comments = extract_likes_comments(snippet)
    title_snippet = f'{title} {snippet}'
    author, link_to_author, post_id = extract_author_post_id(link)


    return (
        entry.get('source', None),
        entry.get('title', None),
        entry.get('snippet', None),
        entry.get('link', None),
        entry.get('thumbnail', None),
        entry.get('video_link', None),
        ', '.join(entry.get('snippet_highlighted_words', [])) if entry.get(
          'snippet_highlighted_words'  
        ) else None,
        entry.get('displayed_link', None),
        title_snippet,
        likes,
        comments,
        author,
        link_to_author,
        post_id
    )

'''
Get items and keys from images results entries

'''
def get_items_from_images_results(entry: Dict) -> Tuple:
    '''
    Extracts and processes specific fields from an image results entry.

    :param entry: A dictionary containing the image results entry.
    :return: A tuple containing the extracted and processed values for the
        fields.
    '''
    # get values
    link = entry.get('link', '')

    # process new fields from data
    author, link_to_author, post_id = extract_author_post_id(link)

    return (
        entry.get('source', None),
        entry.get('title', None),
        entry.get('link', None),
        entry.get('thumbnail', None),
        author,
        link_to_author,
        post_id
    )

'''
Get items and keys from related content entries

'''
def get_items_from_related_content(entry: Dict) -> Tuple:
    '''
    Extracts and processes specific fields from a related content entry.

    :param entry: A dictionary containing the related content entry.
    :return: A tuple containing the extracted and processed values for the
        fields.
    '''
    return (
        entry.get('source', None),
        entry.get('link', None),
        entry.get('thumbnail', None),
        entry.get('title', None)
    )
