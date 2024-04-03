export default function getStudentIdsSum(arrStudents) {
  return arrStudents.reduce((sum, student) => sum + student.id, 0);
}
