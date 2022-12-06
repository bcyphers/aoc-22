print(*[
    list(
        map(
            lambda *e: len(set(e)) == len(e),
            *[open('input').read()[i:-n-i] for i in range(n)]
        )
    ).index(True) + n for n in (4, 14)
])
