Name:           bootchart
Version:        1.20
Release:        1
License:        GPL-2.0
Summary:        Boot time graph generator
Url:            http://meego.gitorious.org/
Group:          Development/Tools
Source0:        bootchart-%{version}.tar.gz

%description
Monitors where the system spends its time at start, creating a graph
of all processes, disk utilization, and wait time.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root,-)
/usr//sbin/bootchartd
%{_datadir}/doc/bootchart/bootchartd.conf.example

%changelog
