export default function getListStudentIds(arrStudents) {
  if (!Array.isArray(arrStudents)) {
    return [];
  }

  return arrStudents.map((student) => student.id);
}
