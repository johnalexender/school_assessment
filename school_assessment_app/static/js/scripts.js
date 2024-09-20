// Function to fetch student data from a text file (or endpoint)
async function fetchStudents() {
    try {
        const response = await fetch('/path/to/student_data.txt'); // Update this path to your Django endpoint
        const data = await response.text();

        // Parse the text data into a student array (assuming the data is formatted as JSON)
        const students = JSON.parse(data); // Adjust parsing based on actual format
        
        return students;
    } catch (error) {
        console.error('Error fetching student data:', error);
        return [];
    }
}

// Function to search for students based on input
async function searchStudent() {
    const input = document.getElementById('searchStudent').value.toLowerCase();
    const tableBody = document.getElementById('studentTable').getElementsByTagName('tbody')[0];
    tableBody.innerHTML = ''; // Clear previous results

    const students = await fetchStudents(); // Fetch student data

    const filteredStudents = students.filter(student => student.fullName.toLowerCase().includes(input));

    if (filteredStudents.length > 0) {
        filteredStudents.forEach(student => {
            const row = `<tr>
                            <td>${student.id}</td>
                            <td>${student.fullName}</td>
                            <td>${student.class}</td>
                            <td>${student.award}</td>
                         </tr>`;
            tableBody.innerHTML += row;
        });
    } else {
        tableBody.innerHTML = '<tr><td colspan="4" class="text-center">No student found</td></tr>';
    }
}