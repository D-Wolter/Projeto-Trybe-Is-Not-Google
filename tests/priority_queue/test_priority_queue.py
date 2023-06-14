from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    pq = PriorityQueue()

    first = {'qtd_linhas': 3}
    second = {'qtd_linhas': 7}
    third = {'qtd_linhas': 4}
    fourth = {'qtd_linhas': 9}

    pq.enqueue(first)
    pq.enqueue(second)
    pq.enqueue(third)
    pq.enqueue(fourth)

    assert len(pq) == 4

    assert pq.search(0) == {"qtd_linhas": 3}
    assert pq.search(1) == {"qtd_linhas": 4}
    assert pq.search(2) == {"qtd_linhas": 7}
    assert pq.search(3) == {"qtd_linhas": 9}

    assert pq.dequeue() == {'qtd_linhas': 3}

    assert len(pq) == 3

    with pytest.raises(IndexError, match='Índice Inválido ou Inexistente'):
        pq.search(-11)
    with pytest.raises(IndexError, match='Índice Inválido ou Inexistente'):
        pq.search(11)
