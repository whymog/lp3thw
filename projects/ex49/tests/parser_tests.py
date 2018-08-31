from nose.tools import *
from ex49 import parser


def test_match():
    assert_equal(parser.match([('direction', 'up')], 'direction'), ('direction', 'up'))
    assert_equal(parser.match([('something', 'nope')], 'nah'), None)

def test_peek():
    assert_equal(parser.peek([('direction', 'south'), ('direction', 'east')]), 'direction')
    assert_equal(parser.peek([]), None)

def test_skip():
    assert_equal(parser.skip([('stop', 'at'), ('stop', 'the'), ('noun', 'planet')], 'stop'), None)
    assert_equal(parser.skip([('stop', 'at'), ('stop', 'the'), ('noun', 'planet')], 'noun'), None)

def test_parse_verb():
    assert_equal(parser.parse_verb([('verb', 'shout')]), ('verb', 'shout'))
    assert_raises(parser.ParserError, parser.parse_verb, [('noun', 'ball')])

def test_parse_object():
    assert_equal(parser.parse_object([('noun', 'prince')]), ('noun', 'prince'))
    assert_equal(parser.parse_object([('direction', 'north')]), ('direction', 'north'))
    assert_raises(parser.ParserError, parser.parse_object, [('verb', 'chortle')])

def test_parse_subject():
    assert_equal(parser.parse_subject([('noun', 'butterfly')]), ('noun', 'butterfly'))
    assert_equal(parser.parse_subject([('verb', 'flutter')]), ('noun', 'player'))
    assert_raises(parser.ParserError, parser.parse_subject, [('direction', 'left')])

def test_parse_sentence():
    assert_equal(parser.parse_sentence([('noun', 'butterfly'), ('stop', 'of'), ('verb', 'drinks'), ('noun', 'soup')]), 
                 parser.Sentence(('noun', 'butterfly'), ('verb', 'drinks'), ('noun', 'soup')))
