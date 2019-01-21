# Ormuco technical test

## A
This question wanted a program which determined if two ranges would overlap.

The ranges needed to be inputted and accepted. This range could have been done in
numerous ways like a list or a tuple. However, I decided to create a class so if
in the future more needed to be added, the freedom and easiness would be there.
Furtheremore, by using a class, it is assured that the method will not encounter
weird cases and issues.  

Finally, a small interface for user input was added with some logic to ensure
the function is getting adequate input.

```
overlaps(rng1: Range, rng2: Range) -> bool
```

## B
This question simply needed to compare two values which were in string form.

This is rather simple as we only need to try to cast the string to a float. If
an error ensues, we can simply catch it and return a different code.

Since this was a library to be imported somewhere else, I added some tests to
ensure that the function was behaving in a proper manner as intended.

```
string_num_cmp(str_num1: str, str_num2: str)-> int
```

## C
This question needed a library which had geo distributed lru cache.

The ExpiringDict is rather similar to the existing OrderedDict. We must simply
add a lock to the dictionary and add the expiration time which is checked when
entries are poped and getten.

Unfortunately, I did not have the time to implement the geo distributed but have
outlined how this would be accomplished. Firstly, each dictionary mush have a
time which it was last updated. This allows us to know which dictionaries are
ahead of the others and even to know if a dictionary is too far behind and must
be totally updatd. Secondly, we need a list of neighbouring nodes to propagate
the changes throughout the network. Since having one way knowledge of nodes is
not ideal, a class for the edges was going to be created to allow both nodes to
know of each other.

Here is an example of how the library would be used:
```
cache = ExpiringDict(cache_len=10, max_age=10)
cache["key"] = "val"
print(cache.get("key"))
```
