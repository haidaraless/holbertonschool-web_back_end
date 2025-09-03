function getStudentIdsSum(arr)
{
    return arr.reduce((sum, item) => sum + item.id, 0);
}

export default getStudentIdsSum;
