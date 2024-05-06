class Star_Cinema:
    def __init__(self):
        self._hall_list = []

    def entry_hall(self, hall):
        self._hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        super().__init__()
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._seats = {}
        self._show_list = []

    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self._show_list.append(show_info)
        self._seats[show_id] = [[0] * self._cols for _ in range(self._rows)]

    def print_seats(self, show_id):
        seats_matrix = self._seats[show_id]
        for row in seats_matrix:
            print('[' + ', '.join(str(seat) for seat in row) + ']')

    def book_seats(self, show_id):
        seats_matrix = self._seats[show_id]
        seat_list = []
        num_seats = int(input("Enter number of tickets: "))

        for num in range(num_seats):
            while True:
                try:
                    row = int(input("Enter seat row: "))
                    col = int(input("Enter seat col: "))

                    if row < 0 or row >= self._rows or col < 0 or col >= self._cols:
                        raise ValueError("Invalid seat")
                    elif seats_matrix[row][col] == 0:
                        seats_matrix[row][col] = 1
                        seat_list.append((row, col))
                        break
                    else:
                        print(f"Seat ({row}, {col}) Already booked.")
                except ValueError:
                    print("Invalid seat. Please enter valid row and column numbers.")

        print("Seats booked successfully:")
        for seat in seat_list:
            print(f"Seat ({row}, {col})")

    def view_show_list(self):
        print("Shows Running:")
        for show in self._show_list:
            show_id, movie_name, time = show
            print(f"Show ID: {show_id}, Movie: {movie_name}, Time: {time}")

    def view_available_seats(self, show_id):
        if show_id in self._seats:
            seats_matrix = self._seats[show_id]
            print(f"Available Seats for Show ID: {show_id}")
            for row in range(self._rows):
                for col in range(self._cols):
                    if seats_matrix[row][col] == 0:
                        print(f"Seat ({row}, {col})")
        else:
            print(f"Show ID: {show_id} does not exist.")


class Counter:
    def __init__(self, cinema):
        self._cinema = cinema

    def view_all_shows(self):
        for hall in self._cinema._hall_list:
            hall.view_show_list()

    def view_available_seats(self, hall_no, show_id):
        for hall in self._cinema._hall_list:
            if hall._hall_no == hall_no:
                hall.view_available_seats(show_id)
                return
        print(f"Hall {hall_no} does not exist.")

    def book_tickets(self, hall_no, show_id):
        for hall in self._cinema._hall_list:
            if hall._hall_no == hall_no:
                try:
                    hall.book_seats(show_id)
                    return
                except KeyError:
                    print(f"Show ID: {show_id} does not exist.")
                    return
        print(f"Hall {hall_no} does not exist.")

def main():
    cinema = Star_Cinema()

    hall1 = Hall(7, 7, 1)
    hall1.entry_show(1, "Mission Impossible", "10:00 AM")
    hall1.entry_show(2, "Ganktoke Gondogol", "2:00 PM")

    hall2 = Hall(6, 6, 2)
    hall2.entry_show(3, "Sherlock Holmes", "5:00 PM")

    cinema.entry_hall(hall1)
    cinema.entry_hall(hall2)

    counter = Counter(cinema)

    while True:
        print("\n--- Star Cinema Ticket Counter ---")
        print("1. View all shows")
        print("2. View available seats in a show")
        print("3. Book tickets in a show")
        print("4. Exit")

        option = input("Select an option: ")

        if option == "1":
            counter.view_all_shows()
        elif option == "2":
            hall_no = int(input("Enter the hall number: "))
            show_id = int(input("Enter the show ID: "))
            counter.view_available_seats(hall_no, show_id)
        elif option == "3":

            hall_no = int(input("Enter the hall number: "))
            show_id = int(input("Enter the show ID: "))
            counter.book_tickets(hall_no, show_id)
        elif option == "4":
            print("Thank you for using the Star Cinema Ticket Counter. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")



main()