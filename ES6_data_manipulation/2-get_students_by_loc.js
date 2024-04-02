export default function getStudentsByLocation(arrStudents, city) {
  return arrStudents.filter((student) => student.location === city);
}
