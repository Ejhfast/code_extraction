# How to read a specific number of integers and store it in a list in python?
n = int(raw_input())
numbers = map(int, raw_input().split())[:n]
