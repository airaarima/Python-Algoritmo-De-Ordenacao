from src.student_template import my_authorial_sort

def main():
    arr = [64, 34, 25, 12, 22, 11, 90,1,7,11,2,9,0]
    print("Vetor Inicial:", arr)
    response = my_authorial_sort(arr)
    print("Vetor Ordenado:", response[0])

if __name__ == "__main__":
    main()