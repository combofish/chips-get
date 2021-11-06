#include <sstream>

const int defaultSize = 16;

// template <typename T> class CStack;
// template <typename T> std::ostream &operator<<(std::ostream &, CStack<T> &);
// template <typename T> std::istream &operator>>(std::istream &, CStack<T> &);

// template <typename T>
// inline std::ostream &operator<<(std::ostream &out_stream, CStack<T> &cstack)
// {
//   T ele;
//   cstack.pop(ele);
//   out_stream << ele;
//   return out_stream;
// }

// template <typename T>
// inline std::istream &operator>>(std::istream &in_stream, CStack<T> &cstack) {
//   T ele;
//   in_stream >> ele;
//   cstack.push(ele);
//   return in_stream;
// }

template <typename T> class CStack {
public:
  CStack(int);
  ~CStack();
  int size() const;
  int capacity() const;
  bool empty();
  bool full();
  bool push(T);
  bool pop(T &);
  T operator[](int);

  template <typename U>
  friend std::ostream &operator<<(std::ostream &out, CStack<U> &);

  template <typename U>
  friend std::istream &operator>>(std::istream &in, CStack<U> &);

  // friend std::ostream &operator<<<>(std::ostream &out, CStack<T> &);
  // friend std::istream &operator>><T>(std::istream &in, CStack<T> &);

  // friend std::ostream &operator<<(std::ostream &out, CStack<T> &cstack) {
  //   T ele;
  //   cstack.pop(ele);
  //   out << ele;
  //   return out;
  // }
  // friend std::istream &operator>>(std::istream &in, CStack<T> &s) {
  //   T ele;
  //   in >> ele;
  //   s.push(ele);
  //   return in;
  // }

  // void print() const;

private:
  void increaseCapacity();

  T *m_pData;
  int m_nTop;
  int m_nBottom;
  int m_nSize;
};

template <typename T> CStack<T>::CStack(int size) {
  if (size <= 0)
    size = defaultSize;

  m_nSize = size;
  m_pData = new T[size];
  m_nTop = m_nBottom = 0;
}

template <typename T> CStack<T>::~CStack() { delete[] m_pData; }

template <typename T> void CStack<T>::increaseCapacity() {
  m_nSize = m_nSize * 2;
  T *tmp_nData = new T[m_nSize];
  for (int i = 0; i < m_nTop; i++) {
    tmp_nData[i] = m_pData[i];
  }
  delete[] m_pData;
  m_pData = tmp_nData;
}

template <typename T> bool CStack<T>::push(T ele) {
  if (full())
    increaseCapacity();

  m_pData[m_nTop++] = ele;
  return true;
}

template <typename T> bool CStack<T>::pop(T &ele) {
  if (empty())
    return false;

  ele = m_pData[--m_nTop];
  return true;
}

template <typename T> bool CStack<T>::full() { return m_nTop >= m_nSize; }

template <typename T> T CStack<T>::operator[](int idx) {
  //  std::cout << "index： " << idx << std::endl;
  if (idx < m_nBottom || idx >= m_nTop)
    std::exit(-1);

  return m_pData[idx];
}

template <typename T>
inline std::ostream &operator<<(std::ostream &out_stream, CStack<T> &cstack) {
  T ele;
  cstack.pop(ele);
  out_stream << ele;
  return out_stream;
}

template <typename T>
inline std::istream &operator>>(std::istream &in_stream, CStack<T> &cstack) {
  T ele;
  in_stream >> ele;
  cstack.push(ele);
  return in_stream;
}

template <typename T> int CStack<T>::capacity() const { return m_nSize; }

/* size() const */
template <typename T> int CStack<T>::size() const { return m_nTop - m_nBottom; }

/* empty() */
template <typename T> bool CStack<T>::empty() {
  return (m_nTop == m_nBottom) ? true : false;
}
