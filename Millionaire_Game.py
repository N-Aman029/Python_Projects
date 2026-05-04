questions = [
    ["Who is Shah Rukh Khan?", "WWE Wrestler", "Actor", "Astronaut", "Plumber", 2],
    ["What is the capital of France?", "Paris", "Rome", "London", "Berlin", 1],
    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],
    ["Which is the largest mammal?", "Elephant", "Blue Whale", "Giraffe", "Shark", 2],
    ["Who wrote 'Romeo and Juliet' ?", "Charles Dickens", "William Shakespeare", "Jane Austen", "Homer", 2],
    ["What is square root of 64?", "8", "4", "7", "9", 1],
    ["Which country is known as the Land of the Rising Sun?", "China", "Japan", "South Korea", "India", 2],
    ["Who painted the Mona Lisa?", "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet", 3],
    ["What is the fastest land animal?", "Cheetah", "Lion", "Elephant", "Horse", 1],
    ["Which ocean is the largest?", "Atlantic Ocean", "Arctic Ocean", "Pacific Ocean", "Indian Ocean", 3],
    ["What is the smallest country in the world?", "Vatican City", "Monaco", "San Marino", "Liechtenstein", 1]
]

Prizes = [100, 200, 400, 900, 2000, 5000, 9000, 18000, 50000, 100000, 500000]

i = 0

for question in questions:
    print(question[0])
    print(f"a.{question[1]}")
    print(f"b.{question[2]}")
    print(f"c.{question[3]}")
    print(f"d.{question[4]}")

    # Check whether the answer is correct or not

    a = int(input("Enter your answer: 1 for a, 2 for b, 3 for c, 4 for d\n"))
    if(a == question[5]):
        print("Correct Answer")

    else:
        print("Better Luck Next time")
        print("correct answer is:", question[5])
        break

    print("You won", Prizes[i])
    i += 1

