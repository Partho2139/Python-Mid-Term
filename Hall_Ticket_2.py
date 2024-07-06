class Star_Cinema:
    def __init__(self):
        self.hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)

    def view_all_shows(self):
        for hall in self.hall_list:
            hall.view_show_list()

    def view_seats(self, hall_no, show_id):
        for hall in self.hall_list:
            if hall.hall_no == hall_no:
                hall.view_available_seats(show_id)
                return
        print(f"Hall number {hall_no} not found.")


class Hall:
    def __init__(self, rows, cols, hall_no, cinema):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        cinema.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show = (id, movie_name, time)
        self.show_list.append(show)
        self.seats[id] = [['free' for _ in range(self.cols)] for _ in range(self.rows)]
        print(f"Show '{movie_name}' added with id '{id}' at {time}.")

    def book_seats(self, show_id, seat_list):
        if show_id not in self.seats:
            print(f"Show ID '{show_id}' not found.")
            return

        for row, col in seat_list:
            if row >= self.rows or col >= self.cols:
                print(f"Seat ({row}, {col}) is invalid.")
                continue
            if self.seats[show_id][row][col] == 'booked':
                print(f"Seat ({row}, {col}) is already booked.")
                continue
            self.seats[show_id][row][col] = 'booked'
            print(f"Seat ({row}, {col}) booked successfully for show ID '{show_id}'.")

    def view_show_list(self):
        if not self.show_list:
            print("No shows available.")
            return
        print(f"Shows in hall {self.hall_no}:")
        for show in self.show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, show_id):
        if show_id not in self.seats:
            print(f"Show ID '{show_id}' not found.")
            return
        print(f"Available seats for show ID '{show_id}':")
        for row in range(self.rows):
            for col in range(self.cols):
                if self.seats[show_id][row][col] == 'free':
                    print(f"({row}, {col}) ", end='')
            print()


def main():
    cinema = Star_Cinema()

    while True:
        print("\n1. Add Hall")
        print("2. Add Show")
        print("3. View All Shows")
        print("4. Book Seats")
        print("5. View Available Seats")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            hall_no = input("Enter hall number: ")
            hall = Hall(rows, cols, hall_no, cinema)
            print(f"Hall {hall_no} added.")

        elif choice == '2':
            hall_no = input("Enter hall number: ")
            for hall in cinema.hall_list:
                if hall.hall_no == hall_no:
                    show_id = input("Enter show ID: ")
                    movie_name = input("Enter movie name: ")
                    time = input("Enter show time: ")
                    hall.entry_show(show_id, movie_name, time)
                    break
            else:
                print(f"Hall number {hall_no} not found.")

        elif choice == '3':
            cinema.view_all_shows()

        elif choice == '4':
            hall_no = input("Enter hall number: ")
            show_id = input("Enter show ID: ")
            seats = []
            while True:
                row = int(input("Enter row number (or -1 to stop): "))
                if row == -1:
                    break
                col = int(input("Enter column number: "))
                seats.append((row, col))
            for hall in cinema.hall_list:
                if hall.hall_no == hall_no:
                    hall.book_seats(show_id, seats)
                    break
            else:
                print(f"Hall number {hall_no} not found.")

        elif choice == '5':
            hall_no = input("Enter hall number: ")
            show_id = input("Enter show ID: ")
            cinema.view_seats(hall_no, show_id)

        elif choice == '6':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
