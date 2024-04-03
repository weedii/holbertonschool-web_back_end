export default function updateStudentGradeByCity(arrStudents, city, newGrades) {
  return arrStudents
    .filter((student) => student.location === city)
    .map((student) => {
      const findGrade = newGrades.find(
        (grade) => grade.studentId === student.id
      );
      if (findGrade) {
        return {
          ...student,
          grade: findGrade.grade,
        };
      } else {
        return {
          ...student,
          grade: 'N/A',
        };
      }
    });
}
