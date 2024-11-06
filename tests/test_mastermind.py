from mastermind.mastermind import make_number, compare_numbers


def test_make_number():
    nums = make_number()
    assert len(nums) == 4
    for x in nums:
        assert 0 <= x <= 9

    nums1 = "".join(map(str, nums))
    nums = make_number()
    nums2 = "".join(map(str, nums))
    assert nums1 != nums2


def test_compare_numbers():
    original_num = [0, 1, 2, 3]
    test_num = [0, 1, 2, 3]
    rez = compare_numbers(original_num, test_num)
    assert rez == (4, 0)

    original_num = [0, 1, 2, 3]
    test_num = [4, 5, 6, 7]
    rez = compare_numbers(original_num, test_num)
    assert rez == (0, 0)

    original_num = [0, 1, 2, 3]
    test_num = [1, 2, 3, 0]
    rez = compare_numbers(original_num, test_num)
    assert rez == (0, 4)

    original_num = [0, 1, 2, 3]
    test_num = [0, 0, 0, 0]
    rez = compare_numbers(original_num, test_num)
    assert rez == (1, 0)

    original_num = [0, 1, 2, 3]
    test_num = [1, 0, 0, 0]
    rez = compare_numbers(original_num, test_num)
    assert rez == (0, 2)

    original_num = [0, 1, 2, 3]
    test_num = [1, 0, 2, 3]
    rez = compare_numbers(original_num, test_num)
    assert rez == (2, 2)
