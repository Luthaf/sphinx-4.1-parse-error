template<typename... T> void parameter_pack(T... u) {}

template <template <class> class HighOrder, typename T>
HighOrder<T> high_order_template() {}
