function updateStudentGradeByCity(students, city, grades)
{
    const newStudents = students.map(student => {
        const grade = grades.find(item => item.studentId == student.id);
        return {...student, grade: (grade) ? grade.grade : 'N/A' };
    }).filter(student => student.location == city);

    return newStudents;
}

export default updateStudentGradeByCity;
