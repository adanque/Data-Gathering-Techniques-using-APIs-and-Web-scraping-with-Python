/*
Author: Alan Danque
Date:	20200920
Purpose:Creates the DSC640_AviationData db objects
*/



use DSC640_AviationData

--if object_id('AviationFatalities') is not null drop table AviationFatalities
go
/*
create table AviationFatalities (
	  rowid int identity(1,1) primary key
	 ,dt datetime default getdate()
	 ,[index] varchar(255)
	 ,Image varchar(255)
	 ,Date varchar(255)
	 ,Operator varchar(255)
	 ,[A/C Type] varchar(255)
	 ,Location varchar(255)
	 ,Fatalities varchar(255)
	 ,Registration varchar(255)
	 ,URL varchar(255)
	 ,PageNum varchar(10)
	)

-- sp_help AviationFatalitiesDetails
--if object_id('AviationFatalitiesDetails') is not null drop table AviationFatalitiesDetails
go
create table AviationFatalitiesDetails (
	 rowid int identity(1,1) primary key
	,src_rowid int
	,dt datetime default getdate()
	,[index] varchar(255)
	,[Date & Time] varchar(255)
	,[Type of aircraft] varchar(255)
	,[Operator] varchar(255)
	,[Registration] varchar(255)
	,[Flight Phase] varchar(255)
	,[Flight Type] varchar(255)
	,[Survivors] varchar(255)
	,[Site] varchar(255)
	,[Schedule] varchar(255)
	,[MSN] varchar(255)
	,[YOM] varchar(255)
	,[Location] varchar(255)
	,[Country] varchar(255)
	,[Region] varchar(255)
	,[Crew on board] varchar(255)
	,[Crew fatalities] varchar(255)
	,[Pax on board] varchar(255)
	,[Pax fatalities] varchar(255)
	,[Other fatalities] varchar(255)
	,[Total fatalities] varchar(255)
	,[Circumstances] varchar(max)
	)
*/


--sp_spaceused
go

select count(*), min(dt), max(dt), max(src_rowid) from AviationFatalitiesDetails  (nolock)
select * from AviationFatalitiesDetails (nolock)

select count(*), min(dt), max(dt), max(cast(PageNum as int)) from AviationFatalities (nolock)
--select count(*), PageNum from AviationFatalities (nolock) group by PageNum order by cast(PageNum as int)

-- Time Lapsed WebScraping
select datediff(mi, min(b.dt), max(b.dt)) / 60.0
						from AviationFatalities a (nolock)
							join AviationFatalitiesDetails b (nolock)
								on a.rowid = b.src_rowid

-- Current status								
-- 1349 Pages of 20
select count(*), a.PageNum, max(b.dt), min(b.dt)
		from AviationFatalities a (nolock)
			join AviationFatalitiesDetails b (nolock)
				on a.rowid = b.src_rowid
			where a.pagenum in (
					select max(cast(PageNum as int)) 
						from AviationFatalities a (nolock)
							join AviationFatalitiesDetails b (nolock)
								on a.rowid = b.src_rowid
					)
	group by a.PageNum

exec sp_spaceused AviationFatalitiesDetails

select top 10 * from AviationFatalitiesDetails (nolock) order by rowid desc

select [type of aircraft], count(*) from AviationFatalitiesDetails (nolock) 
	where [type of aircraft] like '%cessna%'
		and location like '%illinois%'
	group by [type of aircraft] order by count(*) desc

select *
from AviationFatalitiesDetails (nolock) 
	where [type of aircraft] like '%cessna%'
		and location like '%illinois%'

-- my cousins 1989 crash is not in this db. https://www.chicagotribune.com/news/ct-xpm-1989-04-07-8904020056-story.html
select *
from AviationFatalitiesDetails (nolock) 
	where [type of aircraft] like '%cessna 150%'
		and 
		location like '%kankakee%'
		and [date & time] like '%1989%'
		--and [crew on board] = 2
		--and circumstances like '%power%'


select top 10 * from AviationFatalitiesDetails (nolock) where --location like '%ILLINOIS%' and 
	[type of aircraft] like '%cesna%'

select * from AviationFatalitiesDetails (nolock) order by rowid asc

select top 10 * from AviationFatalities (nolock) order by rowid desc



select count(*)
from AviationFatalitiesDetails (nolock) 
-- 26970 rows


select a.[A/C Type], b.[Type of aircraft], * from AviationFatalities a (nolock)
		join AviationFatalitiesDetails b (nolock)
			on a.rowid = b.src_rowid

select rowid as ID, url from AviationFatalities (nolock) order by rowid asc


