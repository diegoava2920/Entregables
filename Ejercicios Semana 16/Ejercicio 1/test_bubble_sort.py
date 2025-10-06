from B_sort import bubble_sort
import pytest

def test_bubble_sort_small_list():
    #AAA
    #Aranmgent
    list_test = [-4, 9, 7, 1, -8 , 4]
    #Argument
    result = bubble_sort(list_test)
    #Assert
    assert result == [-8, -4, 1, 4, 7, 9]

def test_bubble_sort_large_list():
    #AAA
    #Aranmgent
    list_test = [
498, 411, 271, 127, 380, 527, 401, 173, 177, 773,
685, 652, 954, 128, 12, 719, 914, 749, 816, 567,
642, 430, 163, 691, 287, 629, 656, 65, 605, 215,
674, 276, 361, 342, 821, 367, 506, 237, 522, 48,
296, 130, 397, 986, 376, 302, 928, 928, 841, 224,
782, 128, 905, 559, 282, 552, 224, 369, 651, 667,
518, 998, 811, 612, 673, 378, 233, 608, 614, 686,
587, 714, 416, 174, 899, 948, 343, 993, 992, 623,
630, 418, 850, 104, 554, 435, 114, 142, 689, 314,
842, 229, 66, 214, 167, 30, 529, 674, 37, 853
]
    #Argument
    result = bubble_sort(list_test)
    #Assert
    assert result == [
12, 30, 37, 48, 65, 66, 104, 114, 127, 128,
128, 130, 142, 163, 167, 173, 174, 177, 214, 215,
224, 224, 229, 233, 237, 271, 276, 282, 287, 296,
302, 314, 342, 343, 361, 367, 369, 376, 378, 380,
397, 401, 411, 416, 418, 430, 435, 498, 506, 518,
522, 527, 529, 552, 554, 559, 567, 587, 605, 608,
612, 614, 623, 629, 630, 642, 651, 652, 656, 667,
673, 674, 674, 685, 686, 689, 691, 714, 719, 749,
773, 782, 811, 816, 821, 841, 842, 850, 853, 899,
905, 914, 928, 928, 948, 954, 986, 992, 993, 998
]

def test_bubble_sort_empty_list():
    #AAA
    #Aranmgent
    list_test = []
    #Argument
    result = bubble_sort(list_test)
    #Assert
    assert result == []


def test_bubble_sort_only_accepts_list():
    #AAA
    #Aranmgent
    list_test = 123
    #Argument
    #Act Assert
    with pytest.raises(TypeError):
        bubble_sort(list_test)